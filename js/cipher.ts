export const pixel = (num: number) => {
	console.assert(num <= 16777216, "Number should be less than 16777216");

	const b = num;
	const g = Math.floor(num / 256);
	const r = Math.floor(g / 256);

	return [r % 256, g % 256, b % 256];
};

export const visualise = (
	image: HTMLImageElement,
	canvas: HTMLCanvasElement,
	R: number,
	G: number,
	B: number,
	A = 255,
	callback: () => void = console.log,
) => new Promise(res => {
	const width = 400;
	const height = 400;
	const buffer = new Uint8ClampedArray(width * height * 4); // have enough bytes

	for (let y = 0; y < height; y++) {
		for (let x = 0; x < width; x++) {
			const pos = (y * width + x) * 4; // position in buffer based on x and y
			buffer[pos] = R; // some R value [0, 255]
			buffer[pos + 1] = G; // some G value
			buffer[pos + 2] = B; // some B value
			buffer[pos + 3] = A; // set alpha channel
		}
	}

	// create off-screen canvas element
	const canvasContext = canvas.getContext("2d") as CanvasRenderingContext2D;

	canvas.width = width;
	canvas.height = height;

	// create imageData object
	const idata = canvasContext.createImageData(width, height);

	// set our buffer as source
	idata.data.set(buffer);

	// update canvas with new data
	canvasContext.putImageData(idata, 0, 0);

	const dataUri = canvas.toDataURL(); // produces a PNG file

	image.onload = res // optional callback function
	image.src = dataUri;
});

export const readBlob = (file: File, opt_startByte: string, opt_stopByte: string) =>
	new Promise((res) => {
		const start = +opt_startByte || 0;
		const stop = +opt_stopByte || file.size - 1;

		const reader = new FileReader();

		reader.onloadend = (evt) => {
			if (evt.target?.readyState === FileReader.DONE) {
				// DONE == 2
				const a = new Uint8Array(
					(evt.target as { result: ArrayBuffer }).result as ArrayBuffer,
				);
				let binary = "";
				for (let i = 0; i <= a.length; i++) {
					binary += Number(a[i]).toString(2);
				}
				console.log(
					`Read bytes: ${start + 1} - ${stop + 1} of ${file.size} byte file`,
				);

				res({
					binary,
					start: start + 1,
					stop: stop + 1,
					fileSize: file.size,
				});
			}
		};

		const blob = file.slice(start, stop);
		reader.readAsArrayBuffer(blob);
	});

export const onReadInput = async (e: { target: HTMLInputElement }) => {
	const startByte = e.target.dataset.startbyte;
	const endByte = e.target.dataset.endbyte;
	const file = e.target?.files?.[0] as File
	readBlob(file, `${startByte}`, `${endByte}`);
};
/*
const readBytesBtn = document.querySelector(
	"button.readBytesButtons",
) as HTMLButtonElement;

readBytesBtn.addEventListener("click", onReadBtnClick, false);
*/
