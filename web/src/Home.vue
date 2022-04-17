<script>
import { http_request } from "./helpers.js";

export default {
	data() {
		return {
			user: {},
			board_list: [],
			permission: 0,
			edit_permission: {},
			error: "",
		};
	},
	created() {
		const jwt_refresh = localStorage.getItem("jwt_refresh");

		if (jwt_refresh) {
			http_request(
				"get",
				"auth/refresh",
				(data) => {
					localStorage.setItem("jwt", data.access_token);
					localStorage.setItem("jwt_refresh", data.refresh_token);

					this.user = data.current_user;
				},
				this,
				undefined,
				{ Authorization: "Bearer " + jwt_refresh }
			);
		}

		http_request(
			"get",
			"board/list",
			(data) => {
				this.permission = data.permission;
				this.board_list = data.board_list;
			},
			this
		);
	},
	methods: {
		group_board() {
			const data = new FormData();

			const sorted_group = [];

			for (let b of this.board_list) {
				sorted_group.push({ id: b.id, group_id: b.group_id });
			}

			data.append("sorted_group", JSON.stringify(sorted_group));

			http_request(
				"post",
				"board/sort",
				(data) => {
					console.log(data);
				},
				this,
				data
			);
		},
		user_permission() {
			const data = new FormData();

			data.append("user_id", this.edit_permission.user_id);
			data.append("board_id", this.edit_permission.board_id);
			data.append("thread_id", this.edit_permission.thread_id);
			data.append("permission", this.edit_permission.permission);

			http_request(
				"post",
				"auth/permission",
				(data) => {
					console.log(data);
				},
				this,
				data
			);
		},
	},
};
</script>
<template>
	<div class="form">
		<h2>home</h2>
		<div v-if="user.id">
			<span>Welcome! </span>
			<va-avatar :src="user.avartar" size="small" />
			<span>&nbsp;{{ user.username }}</span>
		</div>
		<va-list>
			<va-list-item v-for="(board, index) in board_list" :key="index">
				<va-list-item-section caption>
					<div>
						<router-link :to="'/board/' + board.id">{{
							board.name
						}}</router-link>
						<div v-if="this.permission">
							<va-input
								label="Board group:"
								v-model="board.group_id"
							/>
						</div>
					</div>
				</va-list-item-section>
			</va-list-item>
		</va-list>
		<va-button v-if="this.permission" @click="group_board()"
			>Sort</va-button
		>
		<div v-if="this.permission">
			<va-input label="User id:" v-model="edit_permission.user_id" />
			<va-input label="Board id:" v-model="edit_permission.board_id" />
			<va-input label="Thread id:" v-model="edit_permission.thread_id" />
			<va-input
				label="Permission level:"
				v-model="edit_permission.permission"
			/>
			<va-button @click="user_permission()">Save</va-button>
		</div>
	</div>
</template>
