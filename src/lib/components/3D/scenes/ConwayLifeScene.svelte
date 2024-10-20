<script lang="ts">
	// Import statements
	import { T } from '@threlte/core';
	import { onMount } from 'svelte';
	import { Stars, interactivity } from '@threlte/extras';
	import { catImage } from '$components/3D/parts/cat_image.js';
	import AnimCube from '$components/3D/parts/AnimCube.svelte';

	export let scrollY: number = 0;

	// Types and interfaces
	type PatternType = keyof typeof PATTERNS;
	type Cell = {
		alive: boolean;
		position: [number, number, number];
		height: number;
		targetHeight: number;
		color: string;
	};
	type Grid = Cell[][];

	// Constants
	const PATTERNS = {
		glider: [
			[0, 1, 0],
			[0, 0, 1],
			[1, 1, 1]
		],
		blinker: [[1, 1, 1]]
	};

	// Grid settings
	const gridSettings = {
		items: [
			{ type: 'glider', count: 4 },
			{ type: 'blinker', count: 3 }
		],
		size: 23,
		cellSize: 0.5,
		updateGridTime: 600,
		updateHoverTime: 16
	};

	// Other constants
	const maxHoverHeight = 3 * gridSettings.cellSize;
	const hoverEffectCutoff = 3.5;
	const waveSpeed = 0.4;
	const waveAmplitude = 2 * gridSettings.cellSize;

	// State variables
	let grid: Grid = initializeGrid(gridSettings);
	let hoverPosition: { x: number; y: number } | null = null;
	let previousHoverPosition: { x: number; y: number } | null = null;
	let isImagePainted = false;
	let isWaveInProgress = false;
	let gridUpdateInterval: NodeJS.Timeout | null = null;
	let hoverInterval: NodeJS.Timeout | null = null;

	// Grid initialization functions
	function initializeGrid(settings: typeof gridSettings): Grid {
		const { size, cellSize } = settings;
		let newGrid = createEmptyGrid(size, cellSize);
		newGrid = addPatterns(newGrid, gridSettings.items);
		return newGrid;
	}

	function createEmptyGrid(size: number, cellSize: number): Grid {
		return Array(size)
			.fill(null)
			.map((_, i) =>
				Array(size)
					.fill(null)
					.map((_, j) => ({
						alive: false,
						position: [
							(i - (size - 1) / 2) * cellSize,
							(j - (size - 1) / 2) * cellSize,
							-cellSize / 2
						],
						height: 0,
						targetHeight: 0,
						color: '#1e88e5'
					}))
			);
	}

	function addPatterns(grid: Grid, patternsToAdd: any[]): Grid {
		for (const { type, count } of patternsToAdd as { type: PatternType; count: number }[]) {
			const pattern = PATTERNS[type];
			const patternSize = pattern.length;

			for (let k = 0; k < count; k++) {
				const x = Math.floor(Math.random() * (gridSettings.size - patternSize));
				const y = Math.floor(Math.random() * (gridSettings.size - patternSize));

				for (let i = 0; i < patternSize; i++) {
					for (let j = 0; j < pattern[i].length; j++) {
						// Check if the cell exists before modifying it
						if (grid[x + i] && grid[x + i][y + j]) {
							grid[x + i][y + j].alive = pattern[i][j] === 1;
							if (grid[x + i][y + j].alive) {
								grid[x + i][y + j].position[2] = gridSettings.cellSize / 2;
								grid[x + i][y + j].color = '#1e88e5';
							}
						}
					}
				}
			}
		}
		return grid;
	}

	// Grid update functions
	function updateGrid() {
		grid = grid.map((row, i) =>
			row.map((cell, j) => {
				const neighbors = countNeighbors(i, j);
				const newAlive = cell.alive ? neighbors === 2 || neighbors === 3 : neighbors === 3;
				return {
					...cell,
					alive: newAlive,
					position: [
						cell.position[0],
						cell.position[1],
						(newAlive ? gridSettings.cellSize / 2 : -gridSettings.cellSize / 2) + cell.height
					]
				};
			})
		);

		updateCellHeights();
	}

	function countNeighbors(x: number, y: number) {
		let count = 0;
		for (let i = -1; i <= 1; i++) {
			for (let j = -1; j <= 1; j++) {
				if (i === 0 && j === 0) continue;
				const nx = (x + i + gridSettings.size) % gridSettings.size;
				const ny = (y + j + gridSettings.size) % gridSettings.size;
				if (grid[nx][ny].alive) count++;
			}
		}
		return count;
	}

	function updateCellHeights() {
		const smoothingFactor = 0.2; // Adjust this value to control the speed of the transition
		const hoverChanged = JSON.stringify(hoverPosition) !== JSON.stringify(previousHoverPosition);

		if (hoverPosition && hoverChanged) {
			const { x, y } = hoverPosition;

			for (let i = 0; i < gridSettings.size; i++) {
				for (let j = 0; j < gridSettings.size; j++) {
					const distance = Math.max(Math.abs(x - i), Math.abs(y - j));
					if (distance <= hoverEffectCutoff) {
						const height = maxHoverHeight * (1 - distance / hoverEffectCutoff);
						grid[i][j].targetHeight = height;
					} else {
						grid[i][j].targetHeight = 0;
					}
				}
			}
			previousHoverPosition = { ...hoverPosition };
		} else if (!hoverPosition) {
			for (let i = 0; i < gridSettings.size; i++) {
				for (let j = 0; j < gridSettings.size; j++) {
					grid[i][j].targetHeight = 0;
				}
			}
			previousHoverPosition = null;
		}

		// Smoothly interpolate between current height and target height
		for (let i = 0; i < gridSettings.size; i++) {
			for (let j = 0; j < gridSettings.size; j++) {
				grid[i][j].height += (grid[i][j].targetHeight - grid[i][j].height) * smoothingFactor;
				grid[i][j].position[2] =
					(grid[i][j].alive ? gridSettings.cellSize / 2 : -gridSettings.cellSize / 2) +
					grid[i][j].height;
			}
		}
	}

	// Interval management
	function startIntervals() {
		gridUpdateInterval = setInterval(updateGrid, gridSettings.updateGridTime);
		hoverInterval = setInterval(updateCellHeights, gridSettings.updateHoverTime);
	}

	function stopIntervals() {
		if (gridUpdateInterval) clearInterval(gridUpdateInterval);
		if (hoverInterval) clearInterval(hoverInterval);
		gridUpdateInterval = null;
		hoverInterval = null;
	}

	// Wave effect
	function createWaveEffect(centerX: number, centerY: number) {
		return new Promise<void>((resolve) => {
			const maxDistance = Math.sqrt(2) * gridSettings.size;
			let waveProgress = 0;

			function updateWave() {
				const delta = 5;
				let allCellsAffected = true;

				for (let i = 0; i < gridSettings.size; i++) {
					for (let j = 0; j < gridSettings.size; j++) {
						const distance = Math.sqrt(Math.pow(i - centerX, 2) + Math.pow(j - centerY, 2));
						const waveOffset = Math.max(0, waveAmplitude * (1 - Math.abs(distance - waveProgress)));
						grid[i][j].position[2] = waveOffset;

						if (distance <= waveProgress) {
							if (!isImagePainted) {
								grid[i][j].color = catImage[gridSettings.size - j - 1][i];
								grid[i][j].alive = true;
							} else {
								grid[i][j].alive = false;
								grid[i][j].color = '#1e88e5';
							}
						}

						if (distance + delta > waveProgress) {
							allCellsAffected = false;
						}
					}
				}

				if (!allCellsAffected && waveProgress < maxDistance) {
					waveProgress += waveSpeed;
					requestAnimationFrame(updateWave);
				} else {
					isWaveInProgress = false;
					if (isImagePainted) {
						grid = addPatterns(grid, gridSettings.items);
					}
					resolve();
				}
			}

			updateWave();
		});
	}

	// Event handlers
	function handleClick(rowIndex: number, colIndex: number) {
		if (isWaveInProgress) return; // Don't start a new wave if one is already in progress

		isWaveInProgress = true;
		stopIntervals();

		createWaveEffect(rowIndex, colIndex).then(() => {
			isImagePainted = !isImagePainted;
			if (!isImagePainted) {
				startIntervals();
			} else {
				hoverInterval = setInterval(updateCellHeights, gridSettings.updateHoverTime);
			}
		});
	}

	function handlePointerOver(rowIndex: number, colIndex: number) {
		hoverPosition = { x: rowIndex, y: colIndex };
	}

	function handlePointerLeave() {
		hoverPosition = null;
	}

	onMount(() => {
		grid = initializeGrid(gridSettings);
		startIntervals();
		return stopIntervals;
	});

	interactivity();
</script>

<T.PerspectiveCamera
	makeDefault
	position={[0, -scrollY / 10 - 2, 15 - scrollY / 50]}
	fov={75}
	rotation={[scrollY / 100, 0, 0]}
/>

<T.DirectionalLight position={[3, 10, 10]} intensity={1} />
<T.AmbientLight intensity={1.2} color="#ffffff" />

{#each grid as row, rowIndex}
	{#each row as cell, colIndex}
		<AnimCube
			position={cell.position}
			cellSize={gridSettings.cellSize}
			color={cell.color}
			alive={cell.alive}
			{rowIndex}
			{colIndex}
			{handlePointerOver}
			{handlePointerLeave}
			{handleClick}
		/>
	{/each}
{/each}

<Stars />
