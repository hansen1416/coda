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
			is_admin: false,
			invite_username: "",
			invite_id: 0,
		};
	},
	created() {
		http_request(
			"get",
			"board/front/" + this.$route.params.id,
			(data) => {
				this.name = data.board_name;
				this.permission = data.board_permission;

				this.is_admin = this.permission & (1 << permission_admin);

				this.invite_id = data.invite_id;
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
		invite_mod() {
			const data = new FormData();

			data.append("board_id", this.$route.params.id);
			data.append("username", this.invite_username);

			http_request(
				"post",
				"invite/add",
				(data) => {
					alert("Invitation sent to " + this.invite_username);
				},
				this,
				data
			);
		},
		update_invite(status) {
			const data = new FormData();

			data.append("board_id", this.$route.params.id);
			data.append("invite_id", this.invite_id);
			data.append("status", status);

			http_request(
				"post",
				"invite/update",
				(data) => {
					this.invite_id = 0;
					alert("Invitation updated");
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
		<div v-if="is_admin" style="width: 400px">
			<div>
				<va-input label="Board Name:" v-model="name" />
				<va-button @click="edit_board">Edit</va-button>
			</div>
			<div>
				<va-input label="Invite Moderator:" v-model="invite_username" />
				<va-button @click="invite_mod">Invite</va-button>
			</div>
		</div>
		<div v-if="invite_id" style="width: 400px">
			<div>
				<p>
					You have a moderator invitation from admin {{ invite_id }}
				</p>
				<va-button @click="update_invite(1)">Accept</va-button>
				<va-button @click="update_invite(2)">Reject</va-button>
			</div>
		</div>
	</div>
</template>
