from psychopy import visual, core, gui, event
# Step 2: Now show the dialog box
info = {'Participant': '', 'Age': ''}
dlg = gui.DlgFromDict(dictionary=info, title='Experiment Info')
# Step 1: Create and open the PsychoPy window first
win = visual.Window(fullscr=True, color='grey', units='pix')
win.flip()  # Show the black screen
# Step 3: Show the entered info on the window
message = f"Welcome, {info['Participant']}!\nAge: {info['Age']}"
text_stim = visual.TextStim(win, text=message, color='white')
text_stim.draw()
win.flip()
# Wait for a key press or 3 seconds
event.waitKeys(maxWait=30)
# Cleanup
win.close()
core.quit()