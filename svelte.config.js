import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),

	kit: {
		appDir: 'app',
		adapter: adapter(),
		alias: {
			$components: 'src/lib/components',
			$pages: 'src/lib/pages'
		}
	}
};

export default config;
