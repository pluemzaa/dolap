<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab 3"/>
        <attribute name="authors" value="DELL"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 06:01:58 PM"/>
        <attribute name="created" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswNTozODozOCBQTTsyNjY4"/>
        <attribute name="edited" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswNjowMTo1OCBQTTszOzI3NzE="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <assign variable="i" expression="3"/>
            <assign variable="n" expression="7"/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="&quot; &quot;&amp;i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>