<script>
    import { onMount } from 'svelte';
    import Image from './components/Image.svelte';

    let name = '';

    onMount(async () => {
        const response = await fetch('/hello');
        const data = await response.json();
        name = data.name;
    });
</script>

<main>
    <Image />
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }
</style>