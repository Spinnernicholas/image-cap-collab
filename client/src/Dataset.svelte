<script>
    import Layout from "./Layout.svelte";
    import { onMount } from "svelte";

    let page = 0;
    let pageSize = 12;
    let images = [];

    onMount(async () => {
        const response = await fetch("api/images");
        images = await response.json();
    });
</script>

<Layout>
    <div class="flex flex-wrap">
        {#each images.slice(page * pageSize, (page + 1) * pageSize) as image}
        <div class="w-full md:w-1/2 lg:w-1/4 p-2">
            <a href={`/dataset/${image.id}`}>
            <img
                class="w-full"
                src={`/api/img/${image.filename}`}
                alt={image.filename}
            />
            </a>
        </div>
        {/each}
    </div>
    <div class="flex justify-center m-4">
        {#if page > 0}
            <button class="px-4 py-2 bg-blue-500 text-white rounded" on:click={() => page--}>Previous</button>
        {/if}
        {#if (page + 1) * pageSize < images.length}
            <button class="px-4 py-2 bg-blue-500 text-white rounded" on:click={() => page++}>Next</button>
        {/if}
    </div>
</Layout>
