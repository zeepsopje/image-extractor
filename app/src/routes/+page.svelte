<script context="module">
	import fs from 'fs';
	import { downloadZip } from 'client-zip';
	import colors from '$lib/colors.json';
	import Chart from '$lib/Chart.svelte';
	import hex2hsl from '$lib/hex2hsl';

	async function downloadAll() {
		const elems = Array.from(document.querySelectorAll('canvas'));
		const images = elems.map(canvas => new Promise(resolve => {
			canvas.toBlob(blob => resolve({
				name: canvas.getAttribute('download') + ".png",
				input: blob,
			}));
		}));

		Promise.all(images).then(result => {
			downloadZip(result).blob().then(blob => {
				const link = document.createElement("a")
				link.href = URL.createObjectURL(blob)
				link.download = "colors.zip"
				link.click()
				link.remove()
			});
		});
	}
</script>

<div class="export" on:click={downloadAll}>
	Exporteer alles
</div>

<div class="images">
	{#each Object.entries(colors) as [image, data]}
		<div class="image">
			<img width="200" src="/images/{image}" />
			<div class="data">
				<Chart {data} image_name={image} />
			</div>
		</div>
	{/each}
</div>

<style>
	.export {
		position: fixed;
		top: 30px;
		right: 30px;
	}

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

