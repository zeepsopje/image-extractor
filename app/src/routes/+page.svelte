<script context="module">
	import fs from 'fs';
	import colors from '$lib/colors.json';
	import Chart from '$lib/Chart.svelte';
	import hex2hsl from '$lib/hex2hsl';
</script>

<div class="images">
	{#each Object.entries(colors) as [image, data]}
		<div class="image">
			<img width="200" src="/images/{image}" />
			<div class="data">
				<Chart {data} />
				<div class="bar">
					{#each data.slice(0, 6) as [color]}
						<div class="item" style:background-color={color}></div>
					{/each}
				</div>
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

	.bar {
		display: flex;
		border: solid 1px #000;
	}

	.item {
		width: calc(300px / 6);
	}

	.item::after {
		content: "";
		display: block;
		padding-bottom: 100%;
	}
</style>
