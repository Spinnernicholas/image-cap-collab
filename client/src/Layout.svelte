<script>
</script>

<main style="min-height: 100vh;">
    <header
        class="flex items-center justify-between p-4 bg-gray-800 text-white"
    >
        <a href="/"><h1 class="text-2xl font-bold">ICC Tool</h1></a>
        <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >Login</button
        >
    </header>
    <slot></slot>
    <footer class="flex items-center justify-center p-4 bg-gray-800 text-white">
        <p>&copy; 2022 ICC Tool. All rights reserved.</p>
    </footer>
</main>

<style global lang="postcss">
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
</style>
