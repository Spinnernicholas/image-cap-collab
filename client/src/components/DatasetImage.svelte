<script>
import { onMount } from 'svelte';

export let imageId = 1; // Replace with the actual image ID
let image = {};

onMount(async () => {
    const imageResponse = await fetch(`/api/images/${imageId}`);
    image = await imageResponse.json();
});
</script>

<img class={$$props.class} src={`/api/images/${image.filename}`} alt={image.filename} />