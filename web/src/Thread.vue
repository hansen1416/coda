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
			thread: {},
			permission: "",
			user: {},
			posts: [],
			post_content: "",
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
				this.thread = data.thread;
				this.permission = data.permission;
				this.posts = data.posts;
			},
			this
		);
	},
	methods: {
		delete_post(board_id, thead_id, post_id) {
			const data = new FormData();

			data.append("board_id", board_id);
			data.append("thread_id", thead_id);
			data.append("post_id", post_id);

			http_request(
				"post",
				"post/delete",
				(data) => {
					console.log(data);
				},
				this,
				data
			);
		},
		new_post() {
			const data = new FormData();

			data.append("board_id", this.thread.board_id);
			data.append("thread_id", this.thread.id);
			data.append("content", this.post_content);

			http_request(
				"post",
				"post/add",
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
		<va-alert
			v-if="error"
			color="danger"
			border="top"
			border-color="danger"
		>
			{{ error }}
		</va-alert>
		<va-list>
			<va-list-label>
				{{ thread.title }}
			</va-list-label>
			<va-list-item v-for="(post, index) in posts" :key="index">
				<va-list-item-section caption>
					<div>
						<div>{{ post.content }}</div>
						<div v-if="this.permission">
							<va-button
								@click="
									delete_post(
										post.board_id,
										post.thead_id,
										post.id
									)
								"
								>Delete</va-button
							>
						</div>
					</div>
				</va-list-item-section>
			</va-list-item>
		</va-list>
		<div v-if="user.id" class="form">
			<va-input
				label="Post content"
				v-model="post_content"
				type="textarea"
				:min-rows="3"
				:max-rows="5"
			/>
			<va-button @click="new_post">New Post</va-button>
		</div>
	</div>
</template>
