<script>
import { onMount } from 'svelte';

let imageId = 1; // Replace with the actual image ID
let image = {};
let annotations = [];

onMount(async () => {
    const imageResponse = await fetch(`/api/images/${imageId}`);
    image = await imageResponse.json();

    const annotationsResponse = await fetch(`/api/images/${imageId}/annotations`);
    annotations = await annotationsResponse.json();
});
</script>

<img src={`/api/images/${image.filename}`} alt={image.filename} />

<ul>
    {#each annotations as annotation (annotation.id)}
        <li>{annotation.caption}</li>
    {/each}
</ul>