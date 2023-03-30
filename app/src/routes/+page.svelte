<script context="module">
	import fs from 'fs';
	import colors from '$lib/colors.json';
	import Chart from '$lib/Chart.svelte';
	import hex2hsl from '$lib/hex2hsl';

	let canvas;
</script>

<div class="images">
	{#each Object.entries(colors) as [image, data]}
		<div class="image">
			<img width="200" src="/images/{image}" />
			<div class="data">
				<Chart bind:canvas {data} image_name={image} />
			</div>
		</div>
	{/each}
</div>

<style>
	.images {
		display: flex;
		flex-direction: column;
	}

	.image {
		display: flex;
		flex-direction: row;
		gap: 100px;
	}

	.image img {
		object-fit: contain;
	}

	.color {
		height: 20px;
		width: 20px;
		border: solid 1px #000;
	}
</style>

