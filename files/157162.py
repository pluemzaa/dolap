<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:26:53 PM"/>
        <attribute name="created" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MDY6MDM6MzQgUE07MjIyMQ=="/>
        <attribute name="edited" value="QWRtaW47Q0FSTEFSOzI1NjgtMDctMTY7MDY6MjY6NTMgUE07MjsyMzM2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, s, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="s"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt;= s-n">
                <output expression="n+i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>