<script lang="ts">
	import { AppBar, AppShell } from '@skeletonlabs/skeleton';

    import Hero from '$pages/Hero.svelte';
    import About from '$pages/About.svelte';
    import Projects from '$pages/Projects.svelte';

	// Add these imports for the icons
	import { Linkedin, Github, FileText, Mail } from 'lucide-svelte';

	let scrollY: number = 0;
	let showScrollIndicator: boolean = true;
	let showQuote: boolean = true;
	let isAtBottom: boolean = false;
	let lastActivityTime: number = Date.now();
	let inactivityTimeout: NodeJS.Timeout | null = null;

	const handleScroll = (event: Event) => {
		const target = event.target as HTMLElement;
		scrollY = target.scrollTop;

		showQuote = scrollY <= 15;
		isAtBottom = target.scrollHeight - target.scrollTop === target.clientHeight;

		// Reset activity timer on scroll
		lastActivityTime = Date.now();
		if (inactivityTimeout) {
			clearTimeout(inactivityTimeout);
		}
		setInactivityTimer();

		// Hide scroll indicator immediately when scrolling
		showScrollIndicator = false;
	}
	
	const setInactivityTimer = () => {
		inactivityTimeout = setTimeout(() => {
			if (!isAtBottom) {
				showScrollIndicator = true;
			}
		}, 3000); // Show after 3 seconds of inactivity
	}

	// Initialize inactivity timer
	setInactivityTimer();
</script>

<AppShell on:scroll={handleScroll}>
	<svelte:fragment slot="header">
        <AppBar>
            <svelte:fragment slot="lead">
                <h2 class="h3 md:h2 font-semibold">Alex Li</h2>
            </svelte:fragment>
            <svelte:fragment slot="trail">
                <a class="nav-link" href="https://linkedin.com/in/alexli2002" target="_blank" rel="noopener noreferrer">
                    <span class="hidden sm:inline">LinkedIn</span>
                    <Linkedin class="sm:hidden w-5 h-5" />
                </a>
                <a class="nav-link" href="https://github.com/1liale" target="_blank" rel="noopener noreferrer">
                    <span class="hidden sm:inline">GitHub</span>
                    <Github class="sm:hidden w-5 h-5" />
                </a>
                <a class="nav-link" href='#'>
                    <span class="hidden sm:inline">Resumé</span>
                    <FileText class="sm:hidden w-5 h-5" />
                </a>
                <a class="nav-link" href="mailto:a336li@uwaterloo.ca">
                    <span class="hidden sm:inline">Email</span>
                    <Mail class="sm:hidden w-5 h-5" />
                </a>
            </svelte:fragment>
        </AppBar>
	</svelte:fragment>
	<main class="relative w-full">
		<Hero bind:scrollY={scrollY} bind:showQuote={showQuote}/>
		<About />
		<Projects />

		{#if showScrollIndicator}
			<div class="scroll-indicator">
				<svg class="arrows" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 72">
				<path class="a1" d="M0 0 L30 32 L60 0"></path>
				<path class="a2" d="M0 20 L30 52 L60 20"></path>
				<path class="a3" d="M0 40 L30 72 L60 40"></path>
				</svg>
			</div>
		{/if}
	</main>
</AppShell>

<style>
	.nav-link {
		position: relative;
		text-decoration: none;
		padding: 0.5rem 1rem;
		transition: opacity 0.3s ease-in-out;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	@media (max-width: 639px) {
		.nav-link {
			padding: 0.5rem 0.5rem;
		}
	}

	.nav-link::after {
		content: '';
		position: absolute;
		width: 100%;
		height: 2px;
		bottom: 0;
		left: 0;
		background-color: currentColor;
		transform: scaleX(0);
		transition: transform 0.3s ease-in-out;
	}

	.nav-link:hover::after {
		transform: scaleX(1);
	}

	.scroll-indicator {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .arrows {
    width: 30px;
    height: 36px;
    filter: drop-shadow(0 0 2px #86c2f3);
    animation: glow-flicker 2s infinite;
  }

  .arrows path {
    stroke: #86c2f3;
    fill: transparent;
    stroke-width: 4px;  
    animation: arrow 2s infinite;
  }

  @keyframes arrow {
     0% {opacity:0}
    40% {opacity:1}
    80% {opacity:0}
    100% {opacity:0}
  }

  @keyframes glow-flicker {
    0%, 100% {
      filter: drop-shadow(0 0 2px #86c2f3) drop-shadow(0 0 4px #86c2f3);
    }
    50% {
      filter: drop-shadow(0 0 3px #86c2f3) drop-shadow(0 0 6px #86c2f3) drop-shadow(0 0 9px #86c2f3);
    }
  }

  .arrows path.a1 {
    animation-delay: -1s;
  }

  .arrows path.a2 {
    animation-delay: -0.5s;
  }

  .arrows path.a3 {
    animation-delay: 0s;
  }
</style>
