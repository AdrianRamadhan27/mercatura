/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/**/*.html',
    './**/templates/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
      },
      
      colors: {
        'purple-1': '#5E239D',
        'purple-2': '#150433',
        'purple-3': '#E2DBFD',
        'pink-1': '#F61067',
        'green': '#00F0B5'
      }
    },
  },
  plugins: [],
}
