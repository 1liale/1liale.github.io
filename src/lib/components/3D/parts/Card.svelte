<script lang="ts">
	import { T } from '@threlte/core';
	import {
		ImageMaterial,
		type IntersectionEvent,
		Text,
		Suspense,
		RoundedBoxGeometry
	} from '@threlte/extras';
	import { spring } from 'svelte/motion';
	import BentPlaneGeometry from '$components/3D/parts/BentPlaneGeometry.svelte';
	import { FrontSide, BackSide } from 'three';
	import {
		brightness,
		contrast,
		negative,
		hue,
		saturation,
		lightness,
		monochromeColor,
		monochromeStrength,
		colorProcessingTexture,
		alphaThreshold,
		alphaSmoothing
	} from './props';
	import { interactivity } from '@threlte/extras';
	import { MeshPhysicalMaterial } from 'three';
	interactivity();

	export let index: number;
	export let onCardClick: (index: number) => void;
	export let opacity: number;
	export let isSelected: boolean = false;
	export let content: { title: string, description: string, githubUrl: string, imageUrl: string };
	let hovered = false;

	const scale = spring(1);
	const radius = spring(0.02); // Increased from 0.05 to 0.07
	const zoom = spring(1);

	$: scale.set(isSelected ? 1.3 : hovered ? 1.15 : 1);
	$: radius.set(isSelected ? 0.05 : hovered ? 0.05 : 0.02);

	const stopPropagation =
		(fn: () => void) => (event: IntersectionEvent<'pointerover' | 'pointerleave' | 'click'>) => {
			event.stopPropagation();
			fn();
		};

	const handleClick = () => {
		isSelected = true;
		onCardClick(index);
	};

	const bentPlaneArgs = [
		$radius, // radius
		0.7, // width
		1, // height
		20, // widthSegments
		20 // heightSegments
	];

	let material: MeshPhysicalMaterial;

	$: if (material) {
		material.metalness = 0.5;
		material.roughness = 0.2;
		material.clearcoat = 1;
		material.clearcoatRoughness = 0.1;
		material.reflectivity = 1;
		material.envMapIntensity = 1;
	}

	// New glass material
	let glassMaterial: MeshPhysicalMaterial;

	$: if (glassMaterial) {
		glassMaterial.transparent = true;
		glassMaterial.opacity = isSelected ? 0.8 : 0.35;
		glassMaterial.roughness = 0.5;
		glassMaterial.transmission = 0.5;
		glassMaterial.thickness = 0.2;
		glassMaterial.clearcoat = 1;
		glassMaterial.clearcoatRoughness = 0.1;
		glassMaterial.ior = 1.5;
	}

	// Slightly thicker bent plane args for glass
	const glassPlaneArgs = [
		$radius * 1.01, // slightly larger radius
		bentPlaneArgs[1] * 1.02, // slightly wider
		bentPlaneArgs[2] * 1.02, // slightly taller
		20, // widthSegments
		20 // heightSegments
	];

	// Add these variables for the GitHub button
	let isHovering = false;
	let isPointerDown = false;

	let htmlPosZ = spring(0);
	$: htmlPosZ.set(isPointerDown ? -0.15 : isHovering ? -0.075 : 0, {
		hard: isPointerDown
	});

	// Function to open GitHub link
	const openGitHub = () => {
		window.open(content.githubUrl, '_blank');
	};

	// Add these variables for the GitHub button
	let buttonPosZ = spring(0);
	$: buttonPosZ.set((isPointerDown || isHovering) && isSelected ? -0.01 : 0, {
		hard: isPointerDown
	});

	const cardFrontImages: string[] = [
		'/cards/card_2.png',
		'/cards/card_3.png',
		'/cards/card_4.png',
		'/cards/card_5.png',
		'/cards/card_6.png',
		'/cards/card_7.png',
		'/cards/card_8.png',
		'/cards/card_9.png',
		'/cards/card_10.png',
		'/cards/card_jack.png',
		'/cards/card_queen.png',
		'/cards/card_king.png',
		'/cards/card_ace.png',
	];
</script>

<T.Group scale={$scale} {...$$restProps}>
	<!-- Glass layer with Flex and text -->
	{#if opacity > 0.5}
		<T.Group position.z={0.05}>
			<T.Mesh>
				<BentPlaneGeometry args={glassPlaneArgs} />
				<T.MeshPhysicalMaterial bind:ref={glassMaterial} transparent={true} />
			</T.Mesh>

			<Suspense>
				<T.Group position.z={0.01}>
					<Text
						text={content.title}
						textAlign="center"
						characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
						color="black"
						fillOpacity={0.75 * opacity}
						fontWeight="bold"
						outlineWidth={0.005}
						outlineColor="white"
						outlineOpacity={0.6 * opacity}
						fontSize={0.050}
						position={[0, 0.38, 0.01]}
						anchorX="center"
						anchorY="middle"
					/>

					<!-- Updated Image material plane -->
					<T.Mesh position={[0, 0.12, 0.01]} scale={[0.5, 0.35, 1]}>
						<T.PlaneGeometry args={[1, 1]} radius={$radius} />
						<ImageMaterial
							url={content.imageUrl}
							transparent={true}
							opacity={0.9 * opacity}
							radius={$radius}
						/>
					</T.Mesh>

					<!-- Updated Project description group -->
					<T.Group position={[0, -0.2, 0.02]}>
						<T.Mesh scale={[1.05, 1, 0.01]}>
							<RoundedBoxGeometry args={[0.52, 0.2, 1]} radius={0.02} />
							<T.MeshBasicMaterial color="white" opacity={0.8 * opacity} transparent={true} />
						</T.Mesh>

						<Text
							text={content.description}
							color="black"
							fillOpacity={0.9 * opacity}
							fontSize={0.027}
							position={[-0.25, 0.09, 0.01]}
							maxWidth={0.5}
							textAlign="justify"
						/>
					</T.Group>

					<!-- Updated GitHub button -->
					<T.Group position={[0, -0.38, 0.01]}>
						<T.Mesh
							on:pointerover={() => (isHovering = true)}
							on:pointerleave={() => {
								isHovering = false;
								isPointerDown = false;
							}}
							on:pointerdown={() => (isPointerDown = true)}
							on:pointerup={() => (isPointerDown = false)}
							on:click={isSelected ? openGitHub : null}
							position.z={$buttonPosZ}
							scale.z={0.25}
						>
							<RoundedBoxGeometry args={[0.3, 0.1, 0.01]} radius={0.02} />
							<T.MeshStandardMaterial color="#24292e" {opacity} transparent={true} />
						</T.Mesh>
						<Text
							text="Check it out!"
							color="white"
							fontSize={0.04}
							position={[0, 0, $buttonPosZ + 0.015]}
							anchorX="center"
							anchorY="middle"
							fillOpacity={opacity}
						/>
					</T.Group>
				</T.Group>
			</Suspense>
		</T.Group>
	{/if}

	<!-- Front of the card -->
	<T.Mesh
		on:pointerover={stopPropagation(() => (hovered = true))}
		on:pointerleave={stopPropagation(() => (hovered = false))}
		on:click={stopPropagation(handleClick)}
	>
		<BentPlaneGeometry args={bentPlaneArgs} />
		<ImageMaterial
			side={FrontSide}
			url={cardFrontImages[index]}
			radius={$radius}
			zoom={$zoom}
			alphaThreshold={$alphaThreshold}
			alphaSmoothing={$alphaSmoothing}
			brightness={$brightness}
			contrast={$contrast}
			negative={$negative}
			hue={$hue}
			saturation={$saturation}
			lightness={$lightness}
			monochromeColor={$monochromeColor}
			monochromeStrength={$monochromeStrength}
			colorProcessingTexture={$colorProcessingTexture}
			bind:material
		/>
	</T.Mesh>

	<!-- Back of the card -->
	<T.Mesh>
		<BentPlaneGeometry args={bentPlaneArgs} />

		<ImageMaterial
			transparent={true}
			{opacity}
			side={BackSide}
			url="/cards/card_back.png"
			radius={$radius}
			zoom={$zoom}
			bind:material
		/>
	</T.Mesh>
</T.Group>
