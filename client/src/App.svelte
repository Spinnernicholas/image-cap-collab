<script>
    import { Router, Link, Route } from "svelte-routing";
    import Home from "./Home.svelte";
    import Dataset from "./Dataset.svelte";
    import DatasetItemDetails from "./DatasetItemDetails.svelte";
    import Annotate from "./Annotate.svelte";
</script>

<Router>
    <Route path="/" component={Home} />
    <Route path="/dataset" component={Dataset} />
    <Route path="/dataset/:id" component={DatasetItemDetails} />
    <Route path="/annotate" component={Annotate} />
</Router>
