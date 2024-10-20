<script lang="ts">
	import { AppBar, AppShell, LightSwitch } from '@skeletonlabs/skeleton';
	import { base } from '$app/paths';

    import Hero from '$pages/Hero.svelte';
    import About from '$pages/About.svelte';
    import Projects from '$pages/Projects.svelte';

	// Add these imports for the icons
	import { Linkedin, Github, FileText, Mail } from 'lucide-svelte';

	let scrollY: number = 0;
	let showScrollIndicator: boolean = true;
	let showQuote: boolean = true;

	const handleScroll = (event: Event) => {
        const target = event.target as HTMLElement;
        scrollY = target.scrollTop;

        showScrollIndicator = scrollY <= 70;
        showQuote = scrollY <= 15;
    }
    
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
		<Hero bind:scrollY={scrollY} bind:showScrollIndicator={showScrollIndicator} bind:showQuote={showQuote}/>
		<About />
		<Projects />
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
</style>
