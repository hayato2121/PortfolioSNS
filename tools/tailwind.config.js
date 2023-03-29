/** @type {import('tailwindcss').Config} */
module.exports = {
future: {
  removeDeprecatedGapUtilities: true,
  purgeLayersByDefault: true,
},
purge: {
  enabled: true, //true for production build
  content: ["../templates/**/*.{html,js}"],
},
  theme: {
    extend: {},
  },
  plugins: [],
}
