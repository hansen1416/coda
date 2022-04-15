<script>
import { http_request } from "./helpers.js";

export default {
	data() {
		return {
			error: "",
		};
	},
	created() {
		console.log(this.$route.params.id);
	},
	methods: {},
};
</script>
<template>
	<div>
		<va-alert
			v-if="error"
			color="danger"
			border="top"
			border-color="danger"
		>
			{{ error }}
		</va-alert>
		<div>1111</div>
	</div>
</template>
