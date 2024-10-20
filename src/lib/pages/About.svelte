<script lang="ts">
	import { quintIn } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { ChevronDown } from 'lucide-svelte';
	import Saos from 'saos';
	import Timeline from '$lib/components/Timeline.svelte';
	import timelineData from '$lib/data/timeline.json';
	import { base } from '$app/paths';

	// Import icons from the simple icons collection
	import SvelteIcon from '~icons/simple-icons/svelte';
	import DockerIcon from '~icons/simple-icons/docker';
	import PythonIcon from '~icons/simple-icons/python';
	import TypeScriptIcon from '~icons/simple-icons/typescript';
	import JavaScriptIcon from '~icons/simple-icons/javascript';
	import CplusplusIcon from '~icons/simple-icons/cplusplus';
	import CIcon from '~icons/simple-icons/c';
	import KotlinIcon from '~icons/simple-icons/kotlin';
	import BashIcon from '~icons/simple-icons/gnubash';
	import TensorFlowIcon from '~icons/simple-icons/tensorflow';
	import PyTorchIcon from '~icons/simple-icons/pytorch';
	import PandasIcon from '~icons/simple-icons/pandas';
	import NumPyIcon from '~icons/simple-icons/numpy';
	import ReactIcon from '~icons/simple-icons/react';
	import NextjsIcon from '~icons/simple-icons/nextdotjs';
	import AngularIcon from '~icons/simple-icons/angular';
	import AWSIcon from '~icons/simple-icons/amazonaws';
	import TerraformIcon from '~icons/simple-icons/terraform';
	import GraphQLIcon from '~icons/simple-icons/graphql';
	import MongoDBIcon from '~icons/simple-icons/mongodb';
	import PostgreSQLIcon from '~icons/simple-icons/postgresql';
	import ScikitLearnIcon from '~icons/simple-icons/scikitlearn';
	import HuggingFaceIcon from '~icons/simple-icons/huggingface';
	import VercelIcon from '~icons/simple-icons/vercel';
	import HerokuIcon from '~icons/simple-icons/heroku';
	import CircleCI from '~icons/simple-icons/circleci';
	import RabbitMQIcon from '~icons/simple-icons/rabbitmq';
	import JenkinsIcon from '~icons/simple-icons/jenkins';
	import StripeIcon from '~icons/simple-icons/stripe';
	import GitHubIcon from '~icons/simple-icons/github';

	let expanded = false;
	function toggleExpand() {
		expanded = !expanded;
	}

	// Updated skills data with subtle blue color variations
	const skills = {
		Languages: [
			{ name: 'Python', icon: PythonIcon, color: '#E6F3FF' },
			{ name: 'TypeScript', icon: TypeScriptIcon, color: '#E6F3FF' },
			{ name: 'JavaScript', icon: JavaScriptIcon, color: '#E6F3FF' },
			{ name: 'C++', icon: CplusplusIcon, color: '#E6F3FF' },
			{ name: 'C', icon: CIcon, color: '#E6F3FF' },
			{ name: 'Kotlin', icon: KotlinIcon, color: '#E6F3FF' },
			{ name: 'Bash', icon: BashIcon, color: '#E6F3FF' }
		],
		'AI & ML Tools': [
			{ name: 'TensorFlow', icon: TensorFlowIcon, color: '#E6F3FF' },
			{ name: 'PyTorch', icon: PyTorchIcon, color: '#E6F3FF' },
			{ name: 'Pandas', icon: PandasIcon, color: '#E6F3FF' },
			{ name: 'NumPy', icon: NumPyIcon, color: '#E6F3FF' },
			{ name: 'Scikit-Learn', icon: ScikitLearnIcon, color: '#E6F3FF' },
			{ name: 'HuggingFace', icon: HuggingFaceIcon, color: '#E6F3FF' }
		],
		'Web Technologies': [
			{ name: 'Svelte', icon: SvelteIcon, color: '#E6F3FF' },
			{ name: 'React', icon: ReactIcon, color: '#E6F3FF' },
			{ name: 'Next.js', icon: NextjsIcon, color: '#E6F3FF' },
			{ name: 'Angular', icon: AngularIcon, color: '#E6F3FF' },
			{ name: 'GraphQL', icon: GraphQLIcon, color: '#E6F3FF' },
			{ name: 'MongoDB', icon: MongoDBIcon, color: '#E6F3FF' },
			{ name: 'PostgreSQL', icon: PostgreSQLIcon, color: '#E6F3FF' },
			{ name: 'RabbitMQ', icon: RabbitMQIcon, color: '#E6F3FF' },
			{ name: 'Stripe', icon: StripeIcon, color: '#E6F3FF' }
		],
		'Cloud & DevOps': [
			{ name: 'AWS', icon: AWSIcon, color: '#E6F3FF' },
			{ name: 'Vercel', icon: VercelIcon, color: '#E6F3FF' },
			{ name: 'Heroku', icon: HerokuIcon, color: '#E6F3FF' },
			{ name: 'Docker', icon: DockerIcon, color: '#E6F3FF' },
			{ name: 'Terraform', icon: TerraformIcon, color: '#E6F3FF' },
			{ name: 'CircleCI', icon: CircleCI, color: '#E6F3FF' },
			{ name: 'Jenkins', icon: JenkinsIcon, color: '#E6F3FF' },
			{ name: 'GitHub', icon: GitHubIcon, color: '#E6F3FF' }
		],
		Certifications: [
			{ name: 'AWS Certified Cloud Practitioner', icon: AWSIcon, color: '#E6F3FF' },
			{ name: 'AWS Certified Developer Associate', icon: AWSIcon, color: '#E6F3FF' }
		]
	};
</script>

<section id="about" class="min-h-screen flex items-center justify-center mt-20 mb-40 p-4 md:px-16">
	<Saos animation={'fade-in 1.2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both'}>
		<div
			class="card rounded-lg shadow-lg border-2 border-blue-500/50 overflow-hidden w-full relative flex flex-col"
		>
			<div class="flex flex-col md:flex-row">
				<div class="md:w-2/5">
					<img src="{base}/about/Profile.jpg" alt="Alex Li" class="w-full h-full object-cover" />
				</div>
				<div class="md:w-3/5 p-8 relative">
					<h1 class="text-4xl font-bold mb-4">About Me</h1>
					<p class="text-lg mb-4 text-gray-500">
						I'm a Toronto-based SWE and 4th year undergrad student at the University of Waterloo,
						currently building out innovative health-tech solutions (telemedicine & telehealth) to
						make a positive impact on people's lives.
					</p>

					<p class="text-lg mb-4 text-gray-500">
						I have <strong class="text-blue-500/80">2+ years of working experience </strong>  as a
						full-stack developer and have worked extensively with technologies such as AWS, Docker,
						MongoDB, PostgreSQL, GraphQL, Node.js, Next, SvelteKit, Angular, and many more.
						<span class="info-icon-wrapper">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-5 w-5 inline-block text-blue-500 cursor-help"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
							<span class="tooltip">Expand card to learn more!</span>
						</span>
					</p>

					<p class="text-lg mb-4 text-gray-500">
						Initially, what got me into programming was the excitement from hacking out solutions to
						challenging problems and watching my ideas come to life. With each new project, I gained
						insights and experience that I carried into improving subsequent works.
					</p>

					<p class="text-lg mb-4 text-gray-500">
						I enjoy this iterative process of learning and improving. In many ways, it feels like a
						game where I'm constantly learning and finding new opportunities to be creative and have
						fun with the process!
					</p>

					<div class="absolute top-8 right-8">
						<span class="bg-blue-500/70 text-white text-xs font-semibold px-3 py-2 rounded-full shake-animation">
							⭐ <strong>Seeking New Grad Position May 2025</strong>
						</span>
					</div>
				</div>
			</div>
			<div
				class="relative cursor-pointer"
				role="button"
				tabindex="0"
				aria-label={expanded ? 'Collapse content' : 'Expand content'}
				on:click={toggleExpand}
				on:keydown={(e) => e.key === 'Enter' && toggleExpand()}
			>
				{#if expanded}
					<div transition:slide={{ duration: 1500, easing: quintIn }} class="p-8 relative">
						<hr class="my-6 border-t border-gray-300 dark:border-gray-700" />
						<h3 class="text-3xl font-semibold mb-6">Tools In The Toolbox</h3>

						<div class="space-y-6">
							<Saos animation={'fade-in 1.2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both'}>
								{#each Object.entries(skills) as [category, skillList]}
									<div>
										<h4 class="text-xl font-semibold mb-3">
											{category}
										</h4>
										<div class="flex flex-wrap gap-4">
											{#each skillList as skill}
												<div class="skill-item" title={skill.name}>
													<div class="badge" style="background-color: {skill.color};">
														<svelte:component this={skill.icon} />
													</div>
													<span class="skill-label">{skill.name}</span>
												</div>
											{/each}
										</div>
									</div>
								{/each}
							</Saos>
						</div>

						<hr class="my-6 border-t border-gray-300 dark:border-gray-700" />
						<h3 class="text-3xl font-semibold mb-6">Journey So Far</h3>
						<Timeline {timelineData} />
					</div>
				{/if}
				<div class="gradient-fade">
					<span class="py-4">
						<ChevronDown size={32} class="chevron-icon {expanded ? 'rotate-180' : ''}" />
					</span>
				</div>
			</div>
		</div>
	</Saos>
</section>

<style>
	.gradient-fade {
		position: relative;
		height: 50px;
		background: linear-gradient(to bottom, transparent, #6fb8f5 500%);
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.info-icon-wrapper {
		position: relative;
		display: inline-block;
		bottom: 1px;
	}

	.tooltip {
		visibility: hidden;
		width: 200px;
		background: linear-gradient(to left, #385a9047, #385a90);
		color: #fff;
		text-align: center;
		font-size: 14px;
		border-radius: 6px;
		padding: 5px;
		position: absolute;
		z-index: 1;
		bottom: -5px;
		left: 130px;
		transform: translateX(-50%);
		transition:
			opacity 0.5s,
			visibility 0.5s;
		opacity: 0;
	}

	.info-icon-wrapper:hover .tooltip {
		visibility: visible;
		opacity: 1;
	}

	.badge {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 4rem;
		height: 4rem;
		border-radius: 50%;
		transition: all 0.3s ease;
		padding: 0.5rem;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.badge :global(svg) {
		width: 2.5rem;
		height: 2.5rem;
		margin-bottom: 0.25rem;
		color: #385a90;
	}

	.badge :global(svg) {
		width: 2.5rem;
		height: 2.5rem;
		margin-bottom: 0.25rem;
	}

	.skill-item {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 6rem;
		margin-bottom: 1rem;
	}

	.skill-item:hover {
		transform: scale(1.1);
	}

	.skill-label {
		margin-top: 0.5rem; 
		width: 100%;
		font-size: 0.75rem; 
		text-align: center;
		overflow-wrap: break-word;
		word-wrap: break-word;
		hyphens: auto;
		max-width: 100%;
		line-height: 1.2;
	}

	/* Add the fade-in animation */
	@keyframes -global-fade-in {
		0% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}

	@keyframes shake {
		0%, 100% { transform: rotate(0deg); }
		10%, 30%, 50%, 70%, 90% { transform: rotate(-1.5deg); }
		20%, 40%, 60%, 80% { transform: rotate(1.5deg); }
	}

	.shake-animation:hover {
		cursor: pointer;
		display: inline-block;
		animation: shake 1.2s ease-in-out;
		animation-iteration-count: infinite;
		transform-origin: center;
		font-size: 0.8rem;
	}

</style>

