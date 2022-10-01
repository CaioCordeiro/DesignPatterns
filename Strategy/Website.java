package com.strategy;

public class Website {

	public void login(LoginStrategy loginMethod, String user){
		loginMethod.login(user);
	}
}
