<script>
    import Layout from "./Layout.svelte";
    import { onMount } from "svelte";

    export let id = 1;

    let image = {};
    let annotations = [];

    onMount(async () => {
        const response = await fetch(`/api/images/${id}`);
        if (response.ok) {
            image = await response.json();
        }

        const annotationsResponse = await fetch(
            `/api/images/${id}/annotations`,
        );
        if (annotationsResponse.ok) {
            annotations = await annotationsResponse.json();
        }
    });
</script>

<Layout>
    <div class="flex flex-wrap">
        {#if image.filename}
            <div class="md:w-1/2">
                <img src="/api/img/{image.filename}" alt={image.filename} />
            </div>

            <div class="md:w-1/2 p-4">
                <h1 class="text-center text-2xl font-bold">{image.filename}</h1>
                <h2 class="text-lg font-bold">Annotations</h2>
                <ul>
                    {#each annotations as annotation}
                        <li>
                            <span class="inline-block w-2 h-2 mr-2 rounded-full bg-black"></span>
                            {annotation.caption}
                        </li>
                    {/each}
                </ul>
            </div>
        {/if}
    </div>
</Layout>
