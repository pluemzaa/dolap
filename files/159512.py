<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Fg.num"/>
        <attribute name="authors" value="DELL"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-23 11:19:57 PM"/>
        <attribute name="created" value="REVMTDtERVNLVE9QLUpSSUJPR007MjU2OC0wNy0yMzsxMDowNzowMCBQTTsyNjc5"/>
        <attribute name="edited" value="REVMTDtERVNLVE9QLUpSSUJPR007MjU2OC0wNy0yMzsxMToxOTo1NyBQTTsyOzI4MDQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="numstart" type="Integer" array="False" size=""/>
            <declare name="numend" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="numstart"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="numend"/>
            <while expression="numstart&lt;=numend">
                <output expression="numstart" newline="True"/>
                <assign variable="numstart" expression="numstart+1"/>
            </while>
        </body>
    </function>
</flowgorithm>