<script lang="ts">
  import * as THREE from "three";
  import { T, useTask } from "@threlte/core";
  import { OrbitControls, Suspense } from "@threlte/extras";
  import { onMount } from "svelte";
  import Card from "$components/3D/parts/Card.svelte";
  import projects from "$lib/data/projects.json";

  const rotationSpeed = 0.08;
  const cardCount = 12;
  const radius = 3;
  let carouselGroup: THREE.Group;
  let cards: {
    opacity: number;
    position: THREE.Vector3;
    rotation: THREE.Euler;
    isSelected: boolean;
  }[];
  let isRotating = false;
  let targetRotation = 0;
  let camera: THREE.PerspectiveCamera;
  let initialCameraPosition: THREE.Vector3;
  let targetCameraPosition: THREE.Vector3;
  let isTransitioningCamera = false;
  let selectedCardPosition: THREE.Vector3 | null = null;
  let selectedCardIndex: number | null = null;

  onMount(async () => {
    cards = await createCards();
    initialCameraPosition = new THREE.Vector3(0, 0, 4.25);
    targetCameraPosition = initialCameraPosition.clone();
    isRotating = true;
  });

  const createCards = async () => {
    // Simulate an asynchronous operation (e.g., fetching data)
    await new Promise(resolve => setTimeout(resolve, 500));

    return Array.from({ length: cardCount }, (_, i) => {
      const angle = (i / cardCount) * Math.PI * 2;
      const x = Math.sin(angle) * radius;
      const z = Math.cos(angle) * radius;
      const rotationY = Math.atan2(x, z);
      return {
        position: new THREE.Vector3(x, 0, z),
        rotation: new THREE.Euler(0, rotationY, 0),
        opacity: 1, // Add opacity property
        isSelected: false,
      };
    });
  };

  const updateCardOpacities = () => {
    if (!camera || !carouselGroup) return;

    const cameraPosition = new THREE.Vector3();
    camera.getWorldPosition(cameraPosition);

    cards = cards.map((card, index) => {
      const cardPosition = new THREE.Vector3()
        .copy(card.position)
        .applyMatrix4(carouselGroup.matrixWorld);
      const distance = cardPosition.distanceTo(cameraPosition);
      const maxDistance = radius * 2;
      const normalizedDistance = distance / maxDistance;
      const smoothFactor = 20; // Adjust this value to control the smoothness of the fade
      const opacity = Math.max(
        0.4,
        1 - Math.pow(normalizedDistance, smoothFactor)
      );
      return { ...card, opacity };
    });
  };

  useTask((delta) => {
    if (!carouselGroup || !camera) return;

    // Handle carousel rotation
    if (isRotating) {
      carouselGroup.rotation.y += delta * rotationSpeed;
      carouselGroup.rotation.y %= Math.PI * 2; // Keep the rotation within 0 to 2PI
    } else {
      // Handle camera transition
      if (isTransitioningCamera) {
        const cameraPositionDiff = new THREE.Vector3().subVectors(
          targetCameraPosition,
          camera.position
        );
        const cameraSmoothFactor = 10; // Increased for smoother transition
        const step = Math.min(delta * cameraSmoothFactor, 1);

        if (cameraPositionDiff.length() > 0.001) {
          camera.position.lerp(targetCameraPosition, step);
        } else {
          isTransitioningCamera = false;
        }
        const originPoint = new THREE.Vector3(0, 0, 0);
        camera.lookAt(originPoint);
      } else {
        // Calculate carousel rotation if a card was selected
        if (selectedCardPosition) {
          const cardVector = selectedCardPosition.clone().normalize();
          let angleToRotate = Math.atan2(cardVector.x, cardVector.z);

          // Normalize angle to 0 to 2PI range
          angleToRotate =
            angleToRotate >= 0 ? angleToRotate : 2 * Math.PI + angleToRotate;
          targetRotation = -angleToRotate;

          selectedCardPosition = null;
          cards = cards.map((card, i) => ({
            ...card,
            isSelected: selectedCardIndex !== null && i === selectedCardIndex,
          }));
        }

        // Smoothly rotate to the target rotation
        const diff = targetRotation - carouselGroup.rotation.y;
        const smoothFactor = 0.1; // Adjust this value to control the smoothness of the rotation

        // Determine the shortest rotation path
        let shortestDiff =
          (((diff % (2 * Math.PI)) + 3 * Math.PI) % (2 * Math.PI)) - Math.PI;

        if (Math.abs(shortestDiff) > 0.001) {
          carouselGroup.rotation.y += shortestDiff * smoothFactor;
        } else {
          carouselGroup.rotation.y = targetRotation;
        }
      }
    }

    updateCardOpacities();
  });

  function handleCardClick(index: number) {
    if (!carouselGroup || !camera) return;
    isRotating = false;
    if (selectedCardIndex === index) {
      isRotating = true;
      selectedCardPosition = null;
      selectedCardIndex = null;
      cards[index].isSelected = false;
      return;
    }

    // Set target camera position to initial position
    targetCameraPosition.copy(initialCameraPosition);

    // Store the selected card position for later calculation
    selectedCardPosition = new THREE.Vector3().copy(cards[index].position);
    selectedCardIndex = index;

    isTransitioningCamera = true;
  }
</script>

<T.PerspectiveCamera
  makeDefault
  focus={1.5}
  position={[0, 0, 4.25]}
  fov={75}
  bind:ref={camera}
>
  <OrbitControls
    enablePan={false}
    minPolarAngle={Math.PI / 2 - 0.2}
    maxPolarAngle={Math.PI / 2 + 0.1}
    enableZoom={false}
    minAzimuthAngle={-Math.PI / 16}
    maxAzimuthAngle={Math.PI / 16}
  />
</T.PerspectiveCamera>

<T.AmbientLight intensity={0.75} />
<T.DirectionalLight position={[0, 10, 0]} intensity={0.5} />

<!-- Modify the glossy ground -->
<T.Mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -2.5, 0]}>
  <T.PlaneGeometry args={[100, 100]} />
  <T.MeshPhysicalMaterial
    color="grey"
    metalness={0.4}
    roughness={0.5}
    envMapIntensity={1}
    clearcoat={1}
    clearcoatRoughness={0.5}
    reflectivity={1}
  />
</T.Mesh>

{#if cards}
  <T.Group bind:ref={carouselGroup}>
    {#each cards as card, index (index)}
      <Card
        {index}
        onCardClick={handleCardClick}
        content={projects[index % projects.length]}
        position={[card.position.x, card.position.y, card.position.z]}
        rotation={[card.rotation.x, card.rotation.y, card.rotation.z]}
        opacity={card.opacity}
        isSelected={card.isSelected}
      />
    {/each}
  </T.Group>
{:else}
  <div class="loading">Loading...</div>
{/if}

<style>
  .loading {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 24px;
    font-weight: bold;
  }
</style>
