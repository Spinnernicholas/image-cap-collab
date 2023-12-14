import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';

const production = !process.env.ROLLUP_WATCH;

export default {
    input: 'client/src/main.js',
    output: {
        sourcemap: true,
        format: 'iife',
        name: 'app',
        file: 'public/build/bundle.js'
    },
    plugins: [
      svelte({
        compilerOptions: {
          dev: !production,
        },
        emitCss: false
      }),
      resolve({
        browser: true,
        dedupe: ['svelte']
      }),
      commonjs(),
      !production && livereload('public'),
      production && terser()
    ],
    watch: {
        clearScreen: false
    }
};