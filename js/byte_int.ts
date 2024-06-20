const source_array = new Uint8Array([
	0xff, 0xee, 0xdd, 0xcc, 0xbb, 0xaa, 0x99, 0x88, 0x77, 0x66, 0x55, 0x44, 0x33,
	0x22, 0x11,
]);
const buffer = source_array.buffer;

function method1(buf: Uint8Array | ArrayBufferLike) {
	let bits = 8n;
	if (ArrayBuffer.isView(buf)) {
		bits = BigInt(buf.BYTES_PER_ELEMENT * 8);
	} else {
		buf = new Uint8Array(buf);
	}

	let ret = 0n;
	for (const i of buf.values()) {
		const bi = BigInt(i);
		ret = (ret << bits) + bi;
	}
	return ret;
}
//   input.oninput()

function method2(buf: ArrayBufferLike) {
	const view = new DataView(buf, 0);
	return view.getBigUint64(0, true);
}

function method3(buf: ArrayBufferLike) {
	const arr = new Uint8Array(buf);
	let result = BigInt(0);
	for (let i = arr.length - 1; i >= 0; i--) {
		result = result * BigInt(256) + BigInt(arr[i]);
	}
	return result;
}

// console.log(method1(buffer).toString(16));
console.log(method1(buffer).toString(16));
console.log(method2(buffer).toString(16));
console.log(method3(buffer).toString(16));

function encode(n: bigint) {
	// shift all numbers 1 step to the left and xor if less then 0
	const num = (n << 1n) ^ (n < 0n ? -1n : 0n);

	// convert to hex
	let hex = num.toString(16);
	// pad if neccesseery
	if (hex.length % 2) hex = `0${hex}`;

	// convert hex to bytes
	const hex_match = hex.match(/.{1,2}/g);
	if (hex_match) {
		const bytes = hex_match.map((byte) => Number.parseInt(byte, 16));

		return bytes;
	}
}

function decode(bytes: number[]) {
	// convert bytes back into hex
	const hex = bytes
		.map((e: number) => e.toString(16).padStart(2, "0"))
		.join("");

	// Convert hex to BigInt
	let n = BigInt(`0x${hex}`);

	// Shift all numbers to right and xor if the first bit was signed
	n = (n >> 1n) ^ (n & 1n ? -1n : 0n);

	return n;
}

const test = (value: number) => {
	console.clear();
	const bytes = encode(BigInt(value));
	// TODO: Save or transmit this bytes
	// new Uint8Array(bytes)
	if (bytes) {
		console.log(bytes.join(","));

		const n = decode(bytes);
		console.log(`${n.toString(10)}n`);
	} // cuz SO can't render bigints...
};

export {test}