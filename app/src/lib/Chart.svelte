<script>
	import { onMount } from 'svelte';
	import hex2hsl from '$lib/hex2hsl';

	export let data = [];
	export let image_name = "";

	let canvas;
	let size = 300;
	let padding = 30;
	let range = size - padding;
	let ctx;
	onMount(() => {
		ctx = canvas.getContext('2d');

		// Draw background
		ctx.fillStyle = "#ffffff";
		ctx.fillRect(0, 0, size, size + (size / 6));
		ctx.fillStyle = "#000000";

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

		// Draw bar separator
		ctx.beginPath();
		ctx.moveTo(0, size);
		ctx.lineTo(size, size);
		ctx.stroke();

		[0, 1, 2, 3, 4, 5].forEach(color => {
			ctx.fillStyle = data[color][0];
			ctx.fillRect(
				color * (size / 6),
				size,
				size / 6,
				size / 6,
			);
			ctx.fillStyle = "#000000";
		});

		data.forEach(([hex, occ]) => {
			let { h, l } = hex2hsl(hex);
			let angle = (2 * Math.PI / 255) * (h * 255);
			let center = size / 2;
			let min_rad = 6;
			let max_rad = 70;
			let x = (l * range/2) * Math.cos(angle) + center;
			let y = (l * range/2) * Math.sin(angle) + center;
			ctx.fillStyle = hex;
			ctx.strokeStyle = '#000000';
			ctx.beginPath();
			ctx.arc(
				x, 
				y, 
				((max_rad - min_rad) * occ) + min_rad,
				0,
				2 * Math.PI
			);

			if ((l * range/2) + ((((max_rad - min_rad) * occ) + min_rad)) >= range/2) {
				ctx.stroke();
			}

			ctx.fill();
		});
	});

	function download(e) {
		e.target.download = image_name;
		e.target.href = canvas.toDataURL();
		e.target.click();
		e.target.delete();
	}
</script>

<canvas
	bind:this={canvas}
	width={size}
	height={size + (size / 6)}
	download="image.png"
/>

<a on:click={download}>Download</a>

<style>
	canvas {
		border: solid 1px #000;
	}
</style>
