package com.strategy;

public class UserStrategy implements LoginStrategy {

	private String id;
	private String password;
	
	public UserStrategy(String email, String pwd){
		this.setId(email);
		this.setPassword(pwd);
	}
	
	@Override
	public void login(String id) {
		System.out.println(id + " logged in using his User ID.");
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

}