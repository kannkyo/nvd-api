# Contribution Guide

## Git 設定

### Sign

参考資料を以下に示す。

* https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key
* https://dev.to/devmount/signed-git-commits-in-vs-code-36do
* https://qiita.com/shotakaha/items/65a708f96edbe948eb79

GPG キー作成方法。
ここで、ユーザ名とメールアドレスはコミット時のものと一致し、Git ホスティングサービスに登録したものとも一致していなければならない。
また、GitHub の場合はメールアドレスの検証は不要だが、GitLab の場合は必要である。

```bash
# generate gpg key
gpg --full-generate-key

# check <GPG key ID>
gpg --list-secret-keys --keyid-format=long

# view GPG key
gpg --armor --export <GPG key ID>

# tell key to git
git config --global user.signingkey <GPG key ID>
```
