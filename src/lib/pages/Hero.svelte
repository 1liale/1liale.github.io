<script lang="ts">
  import { fly, fade } from "svelte/transition";
  import { cubicInOut } from "svelte/easing";
  import Typewriter from "$components/Typewriter.svelte";
  import ConwayLifeScene from "$components/3D/scenes/ConwayLifeScene.svelte";
  import { Canvas } from "@threlte/core";

  export let scrollY: number = 0;
  export let showQuote: boolean;

  const messages = [
    "Hi, I'm Alex Li ",
    "I'm a... ",
    "Software Developer ",
    "Problem Solver ",
    "Creative Thinker ",
    "Welcome to my Portfolio! ",
  ];
</script>

<section id="hero" class="min-h-screen flex justify-center">
  {#if showQuote}
    <div class="mt-16" transition:fade={{ duration: 400, easing: cubicInOut }}>
      <Typewriter {messages} delay={60} pauseDelay={800} cycleDelay={5000} />
    </div>
  {/if}
</section>

<div class="absolute w-full inset-0 h-screen">
  <Canvas>
    <ConwayLifeScene bind:scrollY />
  </Canvas>
</div>

{#if showQuote}
  <div
    class="quote-container"
    transition:fade={{ duration: 500, easing: cubicInOut }}
  >
    <blockquote class="quote text-lg lg:text-xl font-semibold">
      "Most people consider life a battle, but it is not a battle, it is a
      game."
    </blockquote>
    <cite class="quote-author text-sm lg:text-base mt-2"
      >- Florence Scovel Shinn</cite
    >
  </div>
{/if}

<style>
  .quote-container {
    position: fixed;
    bottom: 6rem;
    left: 50%;
    transform: translateX(-50%) translateY(-25%);
    text-align: center;
    color: white;
    z-index: 10;
    width: 80%;
    max-width: 800px;
  }

  .quote {
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
  }

  .quote-author {
    display: block;
    margin-top: 0.5rem;
    font-style: italic;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
  }

  /* Add this keyframe animation */
  @keyframes fade-in {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
</style>
