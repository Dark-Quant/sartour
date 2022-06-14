function Panorama () {
    Panorama.superclass.constructor.call(this);

    this.validate();
}

ymaps.util.defineClass(Panorama, ymaps.panorama.Base, {
    // Методы, возвращающие данные панорамы.
	getAngularBBox: function () {
		return [
			0.5 * Math.PI,
			2 * Math.PI,
			-0.5 * Math.PI,
			0
		];
	},
	
	getPosition: function () {
		// Для простоты выберем начало координат в качестве положения панорамы, ...
		return [0, 0];
	},
	getCoordSystem: function () {
		// ...а системой координат выберем декартову, чтоб наша панорама не
		// плавала где-то в Гвинейском заливе.
		return ymaps.coordSystem.cartesian
	},
	getTileSize: function () {
		return [500, 500];
	},
	
	getTileLevels: function () {
		return [
			{
				getTileUrl: function (x, y) {
					return '/hq/' + x + '-' + y + '.jpg';
				},

				getImageSize: function () {
					return [2000, 1000];
				}
			},
			{
				getTileUrl: function (x, y) {
					return '/lq/' + x + '-' + y + '.jpg';
				},

				getImageSize: function () {
					return [512, 256];
				}
			}
		];
	}
});

var player = new ymaps.panorama.Player('player', new Panorama());