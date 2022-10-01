package com.strategy;

public class StrategyClient {
	public static void main(String[] args) {
		Website website = new Website();
		UserStrategy user = new UserStrategy("Stanislau", "1234");
		GmailStrategy gmail = new GmailStrategy("stanislau@gmail.com", "Stanislau");
		
		
		website.login(user, user.getId());

		website.login(gmail, gmail.getId());
	}
}