
class Wimp:
    Null = 0
    RedrawWindow = 1
    OpenWindow = 2
    CloseWindow = 3
    PointerLeavingWindow = 4
    PointerEnteringWindow = 5
    MouseClick = 6
    UserDragBox = 7
    KeyPressed = 8
    MenuSelection = 9
    ScrollRequest = 10
    LoseCaret = 11
    GainCartet = 12
    PollwordNonZero = 13
    UserMessage = 17
    UserMessageRecorded = 18
    UserMessageAcknowledge = 19
    ToolboxEvent = 0x200

    class Poll:
        NullMask                   = (1 << 0)
        RedrawWindowRequestMask    = (1 << 1)
        PointerLeavingWindowMask   = (1 << 4)
        PointerEnteringWindowMask  = (1 << 5)
        MouseClickMask             = (1 << 6)
        KeyPressedMask             = (1 << 8)
        LoseCaretMask              = (1 << 11)
        GainCaretMask              = (1 << 12)
        PollWordNonZeroMask        = (1 << 13)
        UserMessageMask            = (1 << 17)
        UserMessageRecordedMask    = (1 << 18)
        UserMessageAcknowledgeMask = (1 << 19)
        PollWord                   = (1 << 22)
        PollWordHighPriority       = (1 << 23)
        SaveFPRegs                 = (1 << 24)
