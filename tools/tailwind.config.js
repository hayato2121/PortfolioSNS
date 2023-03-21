/** @type {import('tailwindcss').Config} */
module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    content: ["../**/templates/*.html', '../**/templates/**/*.html"],//開発環境
  },
  content: [""],
  plugins: [],
};
