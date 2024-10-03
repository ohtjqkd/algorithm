package programmers;
import java.util.*;
public class SkillTree {

	public void test(String[] args) {
		String skill = "CBD";
		String[] skill_trees = {"BACDE", "CBADF", "AECB", "BDA"};
		SkillTree st = new SkillTree();
		System.out.println(st.solution(skill, skill_trees));
	}
	public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int treeLength = skill_trees.length;

        for(int i=0; i<treeLength; i++){
            boolean flag = true;
            String[] skills = skill_trees[i].split("");
            int cnt=0;

            int skillsLen = skills.length;
            for(int j=0; j<skills.length; j++){
            	System.out.println("CNT는 " + cnt + skills[j] + "의 index" + skill.indexOf(skills[j]));
                if(cnt < skill.indexOf(skills[j])){
                    flag = false;
                    break;
                }else if(cnt == skill.indexOf(skills[j])){
                    cnt++;
                }
            }

            if(flag){
                answer++;
            }
        }
        return answer;
    }

}
