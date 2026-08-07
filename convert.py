import os
import pandas as pd

csv_file = 'Troubleshooting_troubleshooting_EN.csv'
df = pd.read_csv(csv_file)

output_dir = 'ITR'
os.makedirs(output_dir, exist_ok=True) 

df.columns = df.columns.str.strip()

module_col = 'Functional Module'

if module_col in df.columns:
    for module_name, group in df.groupby(module_col):
        if pd.isna(module_name) or not str(module_name).strip():
            continue
        safe_filename = (
            str(module_name)
            .strip()
            .lower()
            .replace(' ', '-')
            .replace('&', '')
            .replace('/','-')
        )
        file_path = os.path.join(output_dir, f'{safe_filename}.md')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f'#{module_name} Troubleshooting\n\n')

            for _, row in group.iterrows():
                symptom = row.get('Primary Symptom', '')
                sub_symptom = row.get('Secondary Symptom', '')
                solution = row.get ('Solution', '')
                error_code = row.get('Related Error Code', '')
                query_page = row.get('Query Page', '')
                models = row.get('Applicable Modules', '')
                if_not_solved = row.get ('If not solved', '')


                title_text = (
                    f'**{symptom}** - {sub_symptom}'
                    if pd.notna(sub_symptom) and sub_symptom
                    else f'**{symptom}**' 
                )
                f.write(f'## {title_text}\n\n')

                if pd.notna(error_code) and str(error_code).strip():
                    f.write('**Error Code:**\n\n')
                    lines = str(error_code).strip().splitlines()
                    for line in lines:
                        clean_line = line.strip()
                        if clean_line:
                            f.write(f'- {clean_line}\n')
                    f.write('\n')

                if pd.notna(solution) and str(solution).strip():
                    f.write('**Solution:**\n\n')
                    lines = str(solution).strip().splitlines()
                    for line in lines:
                        clean_line = line.strip()
                        if clean_line:
                            f.write(f'{clean_line}\n')
                    f.write('\n')

                if pd.notna(query_page) and str(query_page).strip():
                    f.write(f'**Query Page:**\n\n{query_page}\n\n')
                    lines = str(query_page).strip().splitlines()
                    for line in lines:
                        clean_line =line.strip()
                        if clean_line:
                            f.write(f'{clean_line}\n')
                    f.write('\n')

                if pd.notna(if_not_solved) and str(if_not_solved).strip():
                    f.write(f'**If not sloved:**\n `{if_not_solved}`\n\n')

                f.write('---\n\n')    
        print(f'updated:{file_path}')
    print('\n All markdown documents done!')
else:
    print(f"cannot find'{module_col}',please check columnn name of csv document!")