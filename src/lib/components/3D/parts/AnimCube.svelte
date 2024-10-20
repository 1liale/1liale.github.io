<script lang="ts">
	import { T } from '@threlte/core';
	import { Edges, FakeGlowMaterial, type IntersectionEvent, Instance } from '@threlte/extras';

	export let position: [number, number, number];
	export let cellSize: number;
	export let color: string;
	export let alive: boolean;
	export let rowIndex: number;
	export let colIndex: number;
	export let handlePointerOver: (rowIndex: number, colIndex: number) => void;
	export let handlePointerLeave: () => void;
	export let handleClick: (rowIndex: number, colIndex: number) => void;
	export let opacity: number;

	const stopPropagation =
		(fn: () => void) => (event: IntersectionEvent<'pointerover' | 'pointerleave' | 'click'>) => {
			event.stopPropagation();
			fn();
		};
</script>

<T.Mesh {position} visible={opacity > 0.925}>
	<T.BoxGeometry args={[cellSize, cellSize, cellSize]} />
	<T.MeshStandardMaterial {color}/>

	{#if alive}
		<Edges thresholdAngle={20} color="#ccc" scale={1.01} />
	{:else}
		<FakeGlowMaterial falloff={0.5} glowColor="#6fb8f5" />
		<Edges thresholdAngle={20} color="#ccc" scale={1.01} />
	{/if}
	<Instance
		id="inner"
		on:pointerover={stopPropagation(() => handlePointerOver(rowIndex, colIndex))}
		on:pointerleave={stopPropagation(handlePointerLeave)}
		on:click={stopPropagation(() => handleClick(rowIndex, colIndex))}
	/>
</T.Mesh>
