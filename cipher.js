function pixel(num) {
  console.assert(num <= 16777216, "Number should be less than 16777216");

  b = num;
  g = Math.floor(num / 256);
  r = Math.floor(g / 256);

  return [r % 256, g % 256, b % 256];
}

function visualise(R, G, B, A = 255, callback) {
  var width = 400,
    height = 400,
    buffer = new Uint8ClampedArray(width * height * 4); // have enough bytes

  for (var y = 0; y < height; y++) {
    for (var x = 0; x < width; x++) {
      var pos = (y * width + x) * 4; // position in buffer based on x and y
      buffer[pos] = R; // some R value [0, 255]
      buffer[pos + 1] = G; // some G value
      buffer[pos + 2] = B; // some B value
      buffer[pos + 3] = A; // set alpha channel
    }
  }

  // create off-screen canvas element
  var canvas = document.createElement("canvas"),
    ctx = canvas.getContext("2d");

  canvas.width = width;
  canvas.height = height;

  // create imageData object
  var idata = ctx.createImageData(width, height);

  // set our buffer as source
  idata.data.set(buffer);

  // update canvas with new data
  ctx.putImageData(idata, 0, 0);

  var dataUri = canvas.toDataURL(); // produces a PNG file
  image.onload = callback; // optional callback function
  image.src = dataUri;
}
