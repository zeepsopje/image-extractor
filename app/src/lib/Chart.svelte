<script>
	import { onMount } from 'svelte';
	import hex2hsl from '$lib/hex2hsl';

	export let data = [];

	let canvas;
	let size = 300;
	let padding = 30;
	let range = size - padding;
	let ctx;
	onMount(() => {
		ctx = canvas.getContext('2d');

		// Draw hue circle
		ctx.beginPath();
		ctx.arc(size/2, size/2, range/2, 0, 2 * Math.PI);
		ctx.stroke();

		// Draw luminosity axis
		ctx.beginPath();
		ctx.moveTo(0, size/2);
		ctx.lineTo(size, size/2);
		ctx.stroke();
		ctx.beginPath();
		ctx.moveTo(size/2, 0);
		ctx.lineTo(size/2, size);
		ctx.stroke();

		data.forEach(([hex, occ]) => {
			let { h, l } = hex2hsl(hex);
			let angle = (2 * Math.PI / 255) * (h * 255);
			let center = size / 2;
			let min_rad = 10;
			let max_rad = 90;
			let x = (l * range/2) * Math.cos(angle) + center;
			let y = (l * range/2) * Math.sin(angle) + center;
			ctx.fillStyle = hex;
			ctx.strokeStyle = l > 0.3 ? '#000000' : '#ffffff';
			ctx.beginPath();
			ctx.arc(
				x, 
				y, 
				((max_rad - min_rad) * occ) + min_rad,
				0,
				2 * Math.PI
			);
			/* ctx.stroke(); */
			ctx.fill();
		});
	});
</script>

<canvas
	bind:this={canvas}
	width={size}
	height={size}
/>

<style>
	canvas {
		border: solid 1px #000;
	}
</style>
