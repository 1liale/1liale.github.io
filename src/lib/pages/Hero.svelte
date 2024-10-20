<script lang="ts">
	import { fly, fade } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import Typewriter from '$components/Typewriter.svelte';
	import ConwayLifeScene from '$components/3D/scenes/ConwayLifeScene.svelte';
	import { Canvas } from '@threlte/core';

	export let scrollY: number = 0;
	export let showScrollIndicator: boolean;
	export let showQuote: boolean;

	const messages = [
		"Hi, I'm Alex Li ",
		"I'm a... ",
		'Software Developer ',
		'Problem Solver ',
		'Creative Thinker ',
		'Welcome to my Portfolio! '
	];
</script>

<section id="hero" class="min-h-screen flex justify-center" >
    {#if showQuote}
    <div class="mt-16" transition:fade={{ duration: 400, easing: cubicInOut }}>
		<Typewriter {messages} delay={60} pauseDelay={800} cycleDelay={5000} />

    </div>
    {/if}
</section>

{#if showScrollIndicator}
	<div
		class="absolute w-full inset-0 h-screen"
		transition:fade={{ duration: 200, easing: cubicInOut }}
	>
		<div class="w-full h-full" transition:fade={{ duration: 800, easing: cubicInOut }}>
			<Canvas>
				<ConwayLifeScene bind:scrollY />
			</Canvas>
		</div>

		<div class="scroll-indicator">
			<div class="mouse-icon">
				<div class="mouse-button"></div>
			</div>
		</div>
	</div>
{/if}

{#if showQuote}
	<div class="quote-container" transition:fade={{ duration: 500, easing: cubicInOut }}>
		<blockquote class="quote text-lg lg:text-xl font-semibold">
			"Most people consider life a battle, but it is not a battle, it is a game."
		</blockquote>
		<cite class="quote-author text-sm lg:text-base mt-2">- Florence Scovel Shinn</cite>
	</div>
{/if}

<style>
	.scroll-indicator {
		position: fixed;
		bottom: 2rem;
		left: 50%;
		transform: translateX(-50%);
		display: flex;
		flex-direction: column;
		align-items: center;
		color: white;
		font-weight: bold;
	}

	.mouse-icon {
		width: 26px;
		height: 40px;
		border: 2px solid var(--mouse-color, #333);
		border-radius: 20px;
		position: relative;
		animation: glow-flicker 4s ease-in-out infinite;
	}

	.mouse-button {
		width: 4px;
		height: 8px;
		background-color: var(--mouse-color, #333);
		position: absolute;
		top: 8px;
		left: 50%;
		transform: translateX(-50%);
		border-radius: 2px;
		animation:
			scroll 2s infinite,
			glow-flicker 4s ease-in-out infinite;
	}

	:global(.dark) .mouse-icon,
	:global(.dark) .mouse-button {
		--mouse-color: white;
	}

	@keyframes glow-flicker {
		0%,
		100% {
			box-shadow:
				0 0 2px var(--mouse-color, #333),
				0 0 4px var(--mouse-color, #333);
		}
		50% {
			box-shadow:
				0 0 3px var(--mouse-color, #333),
				0 0 6px var(--mouse-color, #333),
				0 0 9px var(--mouse-color, #333);
		}
	}

	@keyframes scroll {
		0% {
			opacity: 1;
			transform: translateX(-50%) translateY(0);
		}
		100% {
			opacity: 0.75;
			transform: translateX(-50%) translateY(3px);
		}
	}

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
</style>
