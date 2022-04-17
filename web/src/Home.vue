<script>
import { http_request } from "./helpers.js";

export default {
	data() {
		return {
			user: {},
			board_list: [],
			permission: 0,
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
						<router-link :to="'/board/front/' + board.id">{{
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
		<va-button @click="group_board()">Sort</va-button>
	</div>
</template>
