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
			title: "",
			permission: "",
			user: {},
		};
	},
	created() {
		http_request(
			"get",
			"auth/me",
			(data) => {
				this.user = JSON.parse(data.current_user);
			},
			this
		);

		http_request(
			"get",
			"thread/read/" + this.$route.params.id,
			(data) => {
				console.log(data);
			},
			this
		);
	},
	methods: {
		edit_board() {
			const data = new FormData();

			data.append("board_id", this.$route.params.id);
			data.append("board_name", this.name);

			http_request(
				"post",
				"board/edit",
				(data) => {
					this.name = data.board_name;
				},
				this,
				data
			);
		},
	},
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
		<div>{{ title }}</div>
	</div>
</template>
