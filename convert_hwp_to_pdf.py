import os
import glob
import sys
import win32com.client as win32
import win32gui
import win32con
import tkinter.messagebox as msgbox
from tkinter import Tk


def hwptopdf():

    # GUI 창 숨기기
    root = Tk()
    root.withdraw()

    # 현재 스크립트가 있는 폴더 기준으로 .hwp 파일 검색
    folder = os.path.dirname(os.path.abspath(sys.argv[0]))
    hwp_files = glob.glob(os.path.join(folder, '**','*.hwp'), recursive=True)

    try:
        
        # 한글 새 문서 가져오기
        hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')
        win32gui.FindWindow(None, "빈 문서 1 - 한글")

        # 한글 프로그램 백그라운드 실행
        hwp.XHwpWindows.Item(0).Visible = False

        # 보안 모듈 경고 방지
        hwp.RegisterModule("FilePathCheckDLL", "FileAuto")

        # 파일 변환
        for hwp_path in hwp_files:
            pdf_path = hwp_path.replace('.hwp', '.pdf')

            try:
                hwp.Open(hwp_path)
                hwp.HAction.GetDefault("FileSaveAsPdf", hwp.HParameterSet.HFileOpenSave.HSet)
                hwp.HParameterSet.HFileOpenSave.filename = pdf_path
                hwp.HParameterSet.HFileOpenSave.Format = "PDF"
                hwp.HAction.Execute("FileSaveAsPdf", hwp.HParameterSet.HFileOpenSave.HSet)

                hwp.HAction.Execute("FileClose")
            except Exception as e:
                print(f"[오류 발생] {hwp_path} → {e}")

        hwp.Quit()
        msgbox.showinfo("알림", "작업이 완료되었습니다.")

    except Exception as err:
        msgbox.showerror("에러", str(err))

# 실행
hwptopdf()
