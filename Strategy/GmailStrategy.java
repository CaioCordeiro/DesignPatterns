package com.strategy;

public class GmailStrategy implements LoginStrategy {

	private String email;
	private String id;
	
	public GmailStrategy(String email, String id){
		this.setEmail(email);
		this.setId(id);
	}
	
	@Override
	public void login(String user) {
		System.out.println(user +" has logged in using Gmail");
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}
}
