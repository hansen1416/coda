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
		<div>{{ name }}</div>
		<div v-if="can_edit" style="width: 400px">
			<va-input label="Board Name:" v-model="name" />
			<va-button @click="edit_board">Edit</va-button>
		</div>
	</div>
</template>
