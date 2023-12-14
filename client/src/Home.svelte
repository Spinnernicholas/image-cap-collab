<script>
    import Layout from "./Layout.svelte";
</script>

<Layout>
    <div class="p-4">
        <div class="grid grid-cols-2 gap-4 align-middle">
            <a
                class="h-40 text-4xl flex items-center justify-center bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                href="/dataset">View Dataset</a
            >
            <a
                class="h-40 text-4xl flex items-center justify-center bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                href="/annotate">Annotate</a
            >
        </div>
    </div>
</Layout>
