#!/usr/bin/env python3
import subprocess

version = "1.0.0-SNAPSHOT"
group_id = "org.jmotor.gradle"
file_path = "dubbo-gradle-plugin/build/libs/dubbo-gradle-plugin-finally.jar"

maven_repo_id = "oss"


class Artifact:
    def __init__(self, id, clazz):
        self.id = id
        self.clazz = clazz


def _exe_cmd(cmd):
    print(cmd)
    subprocess.run(cmd, shell=True)


def _publish_to_local(artifact, archs):
    cmd_install_local = f"mvn install:install-file -Dfile={file_path} -DgroupId={group_id} -DartifactId={artifact.id} -Dversion={version} -Dpackaging=jar"
    _exe_cmd(cmd_install_local)
    for arch in archs:
        _exe_cmd(f"{cmd_install_local} -Dclassifier={arch}")


def _publish_to_central(artifact, archs):
    files = ",".join(map(lambda _arch: file_path, archs))
    types = ",".join(map(lambda _arch: "jar", archs))
    classifiers = ",".join(archs)

    host = "https://oss.sonatype.org"
    if "SNAPSHOT" in version:
        url = f"{host}/content/repositories/snapshots"
    else:
        url = f"{host}/service/local/staging/deploy/maven2"
    cmd_publish = f"mvn deploy:deploy-file -Dfile={file_path} -Dfiles={files} -Dtypes={types} -Dclassifiers={classifiers} -DgroupId={group_id} -DartifactId={artifact.id} -Dversion={version} -Dpackaging=jar -Durl={url} -DrepositoryId={maven_repo_id}"

    _exe_cmd(cmd_publish)


if __name__ == "__main__":
    _exe_cmd("rm -rf dubbo-gradle-plugin/build")
    archs = ["linux-x86_64", "linux-x86_32", "linux-aarch_64", "osx-x86_64", "osx-aarch_64", "windows-x86_32",
             "windows-x86_64"]
    artifacts = [
        Artifact("dubbo-gradle-plugin", "org.jmotor.gradle.DubboGradlePlugin"),
        Artifact("dubbo-grpc-gradle-plugin", "org.jmotor.gradle.DubboGrpcGradlePlugin"),
        Artifact("dubbo-triple-gradle-plugin", "org.jmotor.gradle.DubboTripleGradlePlugin")
    ]

    for artifact in artifacts:
        _exe_cmd(f"gradle fatJar -PmainClass={artifact.clazz}")
        _publish_to_central(artifact, archs)
