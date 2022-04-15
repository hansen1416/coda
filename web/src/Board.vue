<script>
import {
	http_request,
	permission_owner,
	permission_admin,
	permission_mod,
} from "./helpers.js";

export default {
	data() {
		return {
			error: "",
			name: "",
			permission: "",
			can_edit: false,
		};
	},
	created() {
		http_request(
			"get",
			"board/front/" + this.$route.params.id,
			(data) => {
				this.name = data.board_name;
				this.permission = data.board_permission;

				this.can_edit = this.permission & (1 << permission_admin);
			},
			this
		);
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
		<div>{{ name }}</div>
		<va-button v-if="can_edit">Edit</va-button>
	</div>
</template>
