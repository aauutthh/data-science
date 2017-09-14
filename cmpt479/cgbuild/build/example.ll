; ModuleID = '../../callgraph-profiler-template/test/example.c'
source_filename = "../../callgraph-profiler-template/test/example.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [9 x i8] c"Blimey!\0A\00", align 1

; Function Attrs: noinline nounwind uwtable
define void @foo(i32) #0 !dbg !6 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  call void @llvm.dbg.declare(metadata i32* %2, metadata !10, metadata !11), !dbg !12
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str, i32 0, i32 0)), !dbg !13
  ret void, !dbg !14
}

; Function Attrs: nounwind readnone
declare void @llvm.dbg.declare(metadata, metadata, metadata) #1

declare i32 @printf(i8*, ...) #2

; Function Attrs: noinline nounwind uwtable
define void @bar(i32) #0 !dbg !15 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  call void @llvm.dbg.declare(metadata i32* %2, metadata !16, metadata !11), !dbg !17
  %3 = load i32, i32* %2, align 4, !dbg !18
  %4 = icmp sgt i32 %3, 0, !dbg !20
  br i1 %4, label %5, label %8, !dbg !21

; <label>:5:                                      ; preds = %1
  %6 = load i32, i32* %2, align 4, !dbg !22
  %7 = sub nsw i32 %6, 1, !dbg !24
  call void @bar(i32 %7), !dbg !25
  br label %8, !dbg !26

; <label>:8:                                      ; preds = %5, %1
  ret void, !dbg !27
}

; Function Attrs: noinline nounwind uwtable
define i32 @main(i32, i8**) #0 !dbg !28 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i8**, align 8
  %6 = alloca i32, align 4
  %7 = alloca void (i32)*, align 8
  store i32 0, i32* %3, align 4
  store i32 %0, i32* %4, align 4
  call void @llvm.dbg.declare(metadata i32* %4, metadata !34, metadata !11), !dbg !35
  store i8** %1, i8*** %5, align 8
  call void @llvm.dbg.declare(metadata i8*** %5, metadata !36, metadata !11), !dbg !37
  call void @llvm.dbg.declare(metadata i32* %6, metadata !38, metadata !11), !dbg !41
  store i32 0, i32* %6, align 4, !dbg !41
  br label %8, !dbg !42

; <label>:8:                                      ; preds = %19, %2
  %9 = load i32, i32* %6, align 4, !dbg !43
  %10 = icmp ult i32 %9, 10, !dbg !46
  br i1 %10, label %11, label %22, !dbg !47

; <label>:11:                                     ; preds = %8
  call void @llvm.dbg.declare(metadata void (i32)** %7, metadata !49, metadata !11), !dbg !52
  %12 = load i32, i32* %6, align 4, !dbg !53
  %13 = load i32, i32* %4, align 4, !dbg !54
  %14 = urem i32 %12, %13, !dbg !55
  %15 = icmp ne i32 %14, 0, !dbg !56
  %16 = select i1 %15, void (i32)* @foo, void (i32)* @bar, !dbg !56
  store void (i32)* %16, void (i32)** %7, align 8, !dbg !52
  %17 = load void (i32)*, void (i32)** %7, align 8, !dbg !57
  %18 = load i32, i32* %6, align 4, !dbg !58
  call void %17(i32 %18), !dbg !57
  br label %19, !dbg !59

; <label>:19:                                     ; preds = %11
  %20 = load i32, i32* %6, align 4, !dbg !60
  %21 = add i32 %20, 1, !dbg !60
  store i32 %21, i32* %6, align 4, !dbg !60
  br label %8, !dbg !62, !llvm.loop !63

; <label>:22:                                     ; preds = %8
  ret i32 0, !dbg !66
}

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind readnone }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!3, !4}
!llvm.ident = !{!5}

!0 = distinct !DICompileUnit(language: DW_LANG_C99, file: !1, producer: "clang version 4.0.1 (tags/RELEASE_401/final)", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!1 = !DIFile(filename: "../../callgraph-profiler-template/test/example.c", directory: "/home/almac/workspace/sfu-fall2017-assignments/cmpt479/cgbuild/build")
!2 = !{}
!3 = !{i32 2, !"Dwarf Version", i32 4}
!4 = !{i32 2, !"Debug Info Version", i32 3}
!5 = !{!"clang version 4.0.1 (tags/RELEASE_401/final)"}
!6 = distinct !DISubprogram(name: "foo", scope: !1, file: !1, line: 5, type: !7, isLocal: false, isDefinition: true, scopeLine: 5, flags: DIFlagPrototyped, isOptimized: false, unit: !0, variables: !2)
!7 = !DISubroutineType(types: !8)
!8 = !{null, !9}
!9 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!10 = !DILocalVariable(name: "i", arg: 1, scope: !6, file: !1, line: 5, type: !9)
!11 = !DIExpression()
!12 = !DILocation(line: 5, column: 9, scope: !6)
!13 = !DILocation(line: 6, column: 3, scope: !6)
!14 = !DILocation(line: 7, column: 1, scope: !6)
!15 = distinct !DISubprogram(name: "bar", scope: !1, file: !1, line: 11, type: !7, isLocal: false, isDefinition: true, scopeLine: 11, flags: DIFlagPrototyped, isOptimized: false, unit: !0, variables: !2)
!16 = !DILocalVariable(name: "i", arg: 1, scope: !15, file: !1, line: 11, type: !9)
!17 = !DILocation(line: 11, column: 9, scope: !15)
!18 = !DILocation(line: 12, column: 7, scope: !19)
!19 = distinct !DILexicalBlock(scope: !15, file: !1, line: 12, column: 7)
!20 = !DILocation(line: 12, column: 9, scope: !19)
!21 = !DILocation(line: 12, column: 7, scope: !15)
!22 = !DILocation(line: 13, column: 9, scope: !23)
!23 = distinct !DILexicalBlock(scope: !19, file: !1, line: 12, column: 14)
!24 = !DILocation(line: 13, column: 11, scope: !23)
!25 = !DILocation(line: 13, column: 5, scope: !23)
!26 = !DILocation(line: 14, column: 3, scope: !23)
!27 = !DILocation(line: 15, column: 1, scope: !15)
!28 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 19, type: !29, isLocal: false, isDefinition: true, scopeLine: 19, flags: DIFlagPrototyped, isOptimized: false, unit: !0, variables: !2)
!29 = !DISubroutineType(types: !30)
!30 = !{!9, !9, !31}
!31 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !32, size: 64)
!32 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !33, size: 64)
!33 = !DIBasicType(name: "char", size: 8, encoding: DW_ATE_signed_char)
!34 = !DILocalVariable(name: "argc", arg: 1, scope: !28, file: !1, line: 19, type: !9)
!35 = !DILocation(line: 19, column: 10, scope: !28)
!36 = !DILocalVariable(name: "argv", arg: 2, scope: !28, file: !1, line: 19, type: !31)
!37 = !DILocation(line: 19, column: 23, scope: !28)
!38 = !DILocalVariable(name: "i", scope: !39, file: !1, line: 20, type: !40)
!39 = distinct !DILexicalBlock(scope: !28, file: !1, line: 20, column: 3)
!40 = !DIBasicType(name: "unsigned int", size: 32, encoding: DW_ATE_unsigned)
!41 = !DILocation(line: 20, column: 17, scope: !39)
!42 = !DILocation(line: 20, column: 8, scope: !39)
!43 = !DILocation(line: 20, column: 24, scope: !44)
!44 = !DILexicalBlockFile(scope: !45, file: !1, discriminator: 1)
!45 = distinct !DILexicalBlock(scope: !39, file: !1, line: 20, column: 3)
!46 = !DILocation(line: 20, column: 26, scope: !44)
!47 = !DILocation(line: 20, column: 3, scope: !48)
!48 = !DILexicalBlockFile(scope: !39, file: !1, discriminator: 1)
!49 = !DILocalVariable(name: "fptr", scope: !50, file: !1, line: 21, type: !51)
!50 = distinct !DILexicalBlock(scope: !45, file: !1, line: 20, column: 37)
!51 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !7, size: 64)
!52 = !DILocation(line: 21, column: 12, scope: !50)
!53 = !DILocation(line: 21, column: 26, scope: !50)
!54 = !DILocation(line: 21, column: 30, scope: !50)
!55 = !DILocation(line: 21, column: 28, scope: !50)
!56 = !DILocation(line: 21, column: 25, scope: !50)
!57 = !DILocation(line: 22, column: 5, scope: !50)
!58 = !DILocation(line: 22, column: 10, scope: !50)
!59 = !DILocation(line: 23, column: 3, scope: !50)
!60 = !DILocation(line: 20, column: 32, scope: !61)
!61 = !DILexicalBlockFile(scope: !45, file: !1, discriminator: 2)
!62 = !DILocation(line: 20, column: 3, scope: !61)
!63 = distinct !{!63, !64, !65}
!64 = !DILocation(line: 20, column: 3, scope: !39)
!65 = !DILocation(line: 23, column: 3, scope: !39)
!66 = !DILocation(line: 24, column: 3, scope: !28)
