<script lang="ts">
  import { Canvas } from "@threlte/core";
  import Scene from "$components/3D/scenes/ProjectCarouselScene.svelte";
  import { onMount } from "svelte";

  let heroSection: HTMLElement;
  let showCanvas = false;

  onMount(() => {
    heroSection = document.getElementById("hero")!;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          // Show canvas when Hero is not intersecting (scrolled past)
          showCanvas = !entry.isIntersecting;
        });
      },
      {
        threshold: 0.01, // Adjust this value as needed
      }
    );

    if (heroSection) {
      observer.observe(heroSection);
    }

    return () => {
      if (heroSection) {
        observer.unobserve(heroSection);
      }
    };
  });
</script>

<section id="projects" class="w-full min-h-screen">
	{#if showCanvas}
		<Canvas>	
			<Scene />
		</Canvas>
	{/if}
</section>
